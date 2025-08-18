#!/usr/bin/env python
"""
Generate a data‑pipeline graph from Jupyter notebooks.

Features
--------
* Scans all notebooks under `notebooks/` for common file I/O patterns.
* Builds a directed NetworkX graph: files ⇄ notebooks.
* Renders the graph either
    - interactively with PyVis (`--engine pyvis`, outputs HTML), or
    - statically with Graphviz (`--engine dot/neato/twopi`) or NetworkX spring
      layout (`--engine spring`).

Usage
-----
python pipeline_graph.py --root /path/to/project --out pipeline.html --engine pyvis
"""

import argparse
import re
from pathlib import Path
from typing import Set, Tuple

import nbformat
import networkx as nx

# Optional engines
try:
    import graphviz

    GRAPHVIZ_AVAILABLE = True
except ImportError:
    GRAPHVIZ_AVAILABLE = False

try:
    from pyvis.network import Network

    PYVIS_AVAILABLE = True
except ImportError:
    PYVIS_AVAILABLE = False

# ---------------------------------------------------------------------------
# Regex patterns for I/O – extend as needed
# ---------------------------------------------------------------------------

# READ_PATTERNS = [
#    r"read_(csv|parquet|json|excel)\(\s*['\"]([^'\"]+)['\"]",  # pd.read_xxx("file")
#    r"open\(\s*['\"]([^'\"]+)['\"]",  # open("file")
# ]
# WRITE_PATTERNS = [
#    r"to_parquet\(\s*['\"]([^'\"]+)['\"]",
#    r"to_csv\(\s*['\"]([^'\"]+)['\"]",
#    r"to_json\(\s*['\"]([^'\"]+)['\"]",
#    r"to_excel\(\s*['\"]([^'\"]+)['\"]",
# ]

READ_PATTERNS = [
    r"read_(?:csv|parquet|json|excel)\([^)]*?['\"]([^'\"]+\.(?:csv|parquet|json|xlsx?|xlsm))['\"][^)]*\)",
]

WRITE_PATTERNS = [
    r"to_(?:csv|parquet|json|excel)\([^)]*?['\"]([^'\"]+\.(?:csv|parquet|json|xlsx?|xlsm))['\"][^)]*\)",
]


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------
def extract_paths(cell_source: str, patterns) -> Set[str]:
    """Return a set of file paths matching the supplied regex patterns."""
    paths: Set[str] = set()
    for pat in patterns:
        for match in re.findall(pat, cell_source, flags=re.IGNORECASE | re.DOTALL):
            paths.add(match)
    return paths


def analyze_notebook(nb_path: Path) -> Tuple[Set[str], Set[str]]:
    """Return (inputs, outputs) discovered in a notebook."""
    nb = nbformat.read(nb_path, as_version=4)
    inputs, outputs = set(), set()

    for cell in nb.cells:
        if cell.cell_type != "code":
            continue
        src = cell.source
        inputs.update(extract_paths(src, READ_PATTERNS))
        outputs.update(extract_paths(src, WRITE_PATTERNS))

    # print all inputs and outputs for debugging
    if inputs:
        print(f"Inputs in {nb_path.name}: {', '.join(inputs)}")
    if outputs:
        print(f"Outputs in {nb_path.name}: {', '.join(outputs)}")

    return inputs, outputs


def build_graph(project_root: Path) -> nx.DiGraph:
    """Create a directed graph of notebooks and files."""
    notebooks_dir = project_root / "notebooks"
    graph = nx.DiGraph()

    for nb_path in notebooks_dir.rglob("*.ipynb"):
        inputs, outputs = analyze_notebook(nb_path)
        nb_node = f"{nb_path.relative_to(project_root)}"
        graph.add_node(nb_node, node_type="notebook", label=nb_node)

        for in_file in inputs:
            graph.add_node(in_file, node_type="file", label=in_file)
            graph.add_edge(in_file, nb_node)

        for out_file in outputs:
            graph.add_node(out_file, node_type="file", label=out_file)
            graph.add_edge(nb_node, out_file)

    return graph


# ---------------------------------------------------------------------------
# Renderers
# ---------------------------------------------------------------------------
def draw_graph_pyvis(graph: nx.DiGraph, out_path: Path) -> None:
    """Render graph with PyVis to an interactive HTML file."""
    if not PYVIS_AVAILABLE:
        raise RuntimeError("pyvis is not installed – run `pip install pyvis`.")

    net = Network(height="1500px", width="100%", directed=True, bgcolor="#ffffff")
    net.force_atlas_2based()  # nicer layout

    for node, data in graph.nodes(data=True):
        color = "#87CEFA" if data["node_type"] == "notebook" else "#D3D3D3"
        shape = "box" if data["node_type"] == "notebook" else "ellipse"
        net.add_node(node, label=data["label"], color=color, shape=shape)

    for src, dst in graph.edges():
        net.add_edge(src, dst, arrows="to")

    net.show(str(out_path))
    print(f"✅ Interactive graph written to: {out_path}")


def draw_graph_graphviz(graph: nx.DiGraph, out_path: Path, engine: str) -> None:
    """Render graph with Graphviz to PNG/SVG/PDF."""
    if not GRAPHVIZ_AVAILABLE:
        raise RuntimeError("graphviz is not installed – run `pip install graphviz`.")

    dot = graphviz.Digraph(format=out_path.suffix.lstrip("."), engine=engine)
    for node, data in graph.nodes(data=True):
        shape = "box" if data["node_type"] == "notebook" else "ellipse"
        color = "lightblue" if data["node_type"] == "notebook" else "lightgrey"
        dot.node(
            node, label=data["label"], shape=shape, style="filled", fillcolor=color
        )

    for u, v in graph.edges():
        dot.edge(u, v)

    dot.render(out_path.with_suffix(""), cleanup=True)
    print(f"✅ Static graph written to: {out_path}")


def draw_graph_spring(graph: nx.DiGraph, out_path: Path) -> None:
    """Fallback static rendering with NetworkX spring‑layout (PNG)."""
    import matplotlib.pyplot as plt

    pos = nx.spring_layout(graph, k=0.5, seed=42)
    node_colors = [
        "skyblue" if graph.nodes[n]["node_type"] == "notebook" else "lightgrey"
        for n in graph.nodes()
    ]
    nx.draw(
        graph, pos, with_labels=True, node_color=node_colors, font_size=8, arrows=True
    )
    plt.tight_layout()
    plt.savefig(out_path, dpi=300)
    plt.close()
    print(f"✅ Spring‑layout graph written to: {out_path}")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate pipeline graph from notebooks."
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path("."),
        help="Project root containing data/, notebooks/ and output/ folders.",
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=Path("pipeline.html"),
        help="Output file: .html for PyVis or .png/.svg/.pdf for Graphviz/spring.",
    )
    parser.add_argument(
        "--engine",
        choices=["pyvis", "dot", "neato", "twopi", "spring"],
        default="pyvis",
        help=(
            "Rendering engine: "
            "'pyvis' (interactive HTML), "
            "'dot'/'neato'/'twopi' (Graphviz) or "
            "'spring' (NetworkX fallback)."
        ),
    )
    args = parser.parse_args()

    graph = build_graph(args.root)
    if not graph:
        print("⚠️  No notebook dependencies found.")
        return

    if args.engine == "pyvis":
        draw_graph_pyvis(graph, args.out)
    elif args.engine in {"dot", "neato", "twopi"}:
        draw_graph_graphviz(graph, args.out, engine=args.engine)
    else:  # spring
        draw_graph_spring(graph, args.out)


if __name__ == "__main__":
    main()
