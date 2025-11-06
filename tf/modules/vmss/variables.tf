variable "name_prefix" {}
variable "resource_group" {}
variable "location" {}
variable "capacity" { type = number }
variable "tags" { type = map(string) }
