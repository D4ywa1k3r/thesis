#   collects meta_data of the image
def collect_metadata(self):
    self.image = self.client.images.get(self.img_name)
    self.img_meta = str(self.image.history())