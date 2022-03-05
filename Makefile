mount:
	@sudo mkdir -p /media/${USER}/system-boot /media/${USER}/writable
	sudo mount /dev/sdc1 /media/${USER}/system-boot
	sudo mount /dev/sdc2 /media/${USER}/writable

umount:
	sudo umount /media/${USER}/system-boot /media/${USER}/writable
	@sudo rmdir /media/${USER}/system-boot /media/${USER}/writable

flash:
	@sudo dd if=ubuntu/ubuntu-21.10-preinstalled-server-arm64+raspi.img of=/dev/sdc bs=4M conv=fsync status=progress

configure: mount
	sudo cp user-data.yaml /media/${USER}/system-boot/user-data
