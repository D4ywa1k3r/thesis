def get_lower_directories(self):
    result = []
    for root, dirs, files in os.walk(self.overlay_path):
        if self.lower_file in files:
            fo = open(f"{root}/{self.lower_file}", "r")
            result.append(fo.readline())

    return max(result, key=len)