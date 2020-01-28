def mount_overlay(self):
    self.remove_overlay_dirs()
    self.create_overlay_dirs()
    directory_diffs = self.get_lower_directories()
    mount_cmd = f"mount -t overlay -o lowerdir={directory_diffs},upperdir=./{self.merged_dir_name},workdir=./{self.work_dir_name} {self.overlay_name} {self.merged_dir_name}/"
    os.chdir(self.overlay_path)
    os.system(mount_cmd)