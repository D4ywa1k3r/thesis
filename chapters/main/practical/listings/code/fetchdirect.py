#   set targets for ADD and COPY
def fetch_direct_copy_targets(self):
    temp_list = list()
    for match in re.finditer("(dir|file):[a-f0-9]{64}\sin\s", self.img_meta):
        temp_list.append(self.img_meta[match.span()[1]:self.img_meta.find("'", match.span()[1]) - 1])

    # has to be removed because of trusted upper base layer
    temp_list.remove('/')
    return temp_list