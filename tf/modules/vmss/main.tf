resource "azurerm_linux_virtual_machine_scale_set" "this" {
  name                = "${var.name_prefix}-vmss"
  resource_group_name = var.resource_group
  location            = var.location
  sku                 = "Standard_B2s"
  instances           = var.capacity
  admin_username      = "azureuser"

  source_image_reference {
    publisher = "Canonical"
    offer     = "0001-com-ubuntu-server-jammy"
    sku       = "22_04-lts"
    version   = "latest"
  }

  admin_ssh_key {
    username   = "azureuser"
    public_key = fileexists("~/.ssh/id_rsa.pub") ? file("~/.ssh/id_rsa.pub") : ""
  }

  os_disk {
    caching              = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }

  upgrade_mode = "Manual"

  tags = var.tags
}
