def contains_key_actions(self):
    for key in self.action_dict.keys():
        if key in self.img_meta:
            self.action_dict.update({key: True})

    for value in self.action_dict.values():
        if value is True:
            return True

    return False
