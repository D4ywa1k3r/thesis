def unmount_overlay(self):
    umount_cmd = f"umount {self.overlay_name}"
    os.system(umount_cmd)
