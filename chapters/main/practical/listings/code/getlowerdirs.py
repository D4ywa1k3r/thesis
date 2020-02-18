def get_lower_directories(self):
    dirs = os.listdir(self.overlay_path + '/l')
    lower_chain = ""
    for dir in dirs:
        lower_chain += f"l/{dir}:"

    lower_chain = lower_chain[:len(lower_chain) - 1]
    return lower_chain