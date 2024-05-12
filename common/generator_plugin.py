def plugin(class_list):
    f = open("/content/plugin.py", "w")
    for tool in class_list:
        f.write(f"from {tool}.{tool} import Plugin as {tool.upper()}\n")
    f.write("\n\n")
    f.write("def load_ipython_extension(ip):\n")
    for tool in class_list:
        f.write(f"\tip.register_magics({tool.upper()}(ip))\n")
    f.write("\n")
    f.close()