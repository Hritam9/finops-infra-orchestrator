variable "location" {
  type    = string
  default = "eastus"
}
variable "vmss_capacity" {
  type    = number
  default = 2
}
variable "tags" {
  type    = map(string)
  default = {}
}
