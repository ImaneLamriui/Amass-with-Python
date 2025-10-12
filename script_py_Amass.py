>....                                                                                                                                                             
        if pd != h:
            if pd not in G:
                G.add_node(pd, label=pd, group='parent')
            G.add_edge(h, pd, relation='parent')

    # construir red PyVis
    net = Network(height='800px', width='100%')
    net.from_nx(G)

    # estilo sencillo: tamaño por grado, color por tipo
    for n in net.nodes:
        nid = n['id']
        grp = G.nodes[nid].get('group','host')
        deg = G.degree[nid]
        n['title'] = f"{nid} (degree: {deg})"
        n['value'] = deg + 1
        if grp == 'parent':
            n['color'] = '#ffcc00'
            n['size'] = 18
        else:
            n['color'] = '#6cace4'
            n['size'] = 12 + min(deg,10)

    # Escribir HTML sin el modo "notebook" (evita el bug que dio error)
    net.write_html(args.out, notebook=False)
    print("[+] Grafo generado:", args.out)

if __name__ == '__main__':
    main()
PY

chmod +x build_graph_from_combined.py
echo "Script sobrescrito y marcado ejecutable."
Script sobrescrito y marcado ejecutable.
