def examine_with_specific_option(self, option, pos):
    keygen_option_pos = self.img_meta.find(option, pos)
    examine_string = self.img_meta[keygen_option_pos:]

    #  find 'option' -> start at pos of len(option) and create a substring to whitespace
    end_pos_temp_string = examine_string.find(' ', len(option) + 1)
    examine_string = examine_string[len(option) + 1:end_pos_temp_string]
    if ',' in examine_string:
        examine_string = examine_string[:-2]

    return examine_string