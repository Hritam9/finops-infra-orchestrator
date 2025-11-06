resource "azurerm_resource_group" "this" {
  name     = var.name
  location = var.location
  tags     = var.tags
}

output "name" {
  value = azurerm_resource_group.this.name
}

variable "name" {}
variable "location" {}
variable "tags" {
  type    = map(string)
  default = {}
}
