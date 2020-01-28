#   stop potential running containers
def stop_all_containers(self):
    for container in self.client.containers.list():
        container.reload()
        container.stop()

#   remove old images
def remove_old_images(self):
    for img in self.client.images.list():
        self.client.images.remove(str(img.id), force=True)

#   pull image
def pull_image(self):
    self.client.images.pull(self.img_name + ':latest')