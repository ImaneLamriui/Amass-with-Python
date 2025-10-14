#!/usr/bin/env python3
"""
build_graph_from_combined.py
Genera un grafo interactivo (HTML) a partir de una lista de subdominios.
Uso:
  python build_graph_from_combined.py data/combined.txt --out output/grafo.html
"""

import argparse
import networkx as nx
from pyvis.network import Network

def main():
    parser = argparse.ArgumentParser(description="Crear grafo de subdominios con PyVis")
    parser.add_argument("input", help="Archivo con subdominios (uno por línea)")
    parser.add_argument("--out", default="output/grafo.html", help="Archivo HTML de salida")
    args = parser.parse_args()

    G = nx.Graph()

    with open(args.input) as f:
        for line in f:
            host = line.strip().lower()
            if not host or "." not in host:
                continue
            parts = host.split(".")
            if len(parts) < 2:
                continue
            parent = ".".join(parts[-2:])  # dominio padre (ej: example.com)
            G.add_node(host)
            if parent != host:
                G.add_node(parent)
                G.add_edge(host, parent)

    # Crear visualización
    net = Network(height="800px", width="100%")
    net.from_nx(G)

    # Colores simples
    for node in net.nodes:
        deg = G.degree[node['id']]
        node['value'] = deg + 1
        node['color'] = "#6cace4" if "." in node['id'] else "#ffcc00"
        node['title'] = f"{node['id']} (conexiones: {deg})"

    net.write_html(args.out, notebook=False)
    print(f"[+] Grafo generado en: {args.out}")

if __name__ == "__main__":
    main()
