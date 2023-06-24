mount:
	@sudo mkdir -p /media/${USER}/system-boot /media/${USER}/writable
	sudo mount /dev/sdc1 /media/${USER}/system-boot
	sudo mount /dev/sdc2 /media/${USER}/writable

umount:
	sudo umount /media/${USER}/system-boot /media/${USER}/writable
	@sudo rmdir /media/${USER}/system-boot /media/${USER}/writable

flash:
	@sudo dd if=bootstrap/ubuntu-22.04.2-preinstalled-server-arm64+raspi.img of=/dev/sdc bs=4M conv=fsync status=progress

configure: mount
	sudo cp bootstrap/user-data.yaml /media/${USER}/system-boot/user-data
	sudo cp bootstrap/network-config.yaml /media/${USER}/system-boot/network-config

ansible:
	ansible-playbook -i inventory.yml playbook.yml

ansible-deps:
	ansible-galaxy role install -r roles/requirements.yml
