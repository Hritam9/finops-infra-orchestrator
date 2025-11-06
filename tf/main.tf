module "rg" {
  source   = "./modules/rg"
  name     = "rg-finops-demo"
  location = var.location
  tags     = var.tags
}

module "vmss" {
  source            = "./modules/vmss"
  name_prefix       = "finops"
  resource_group    = module. rg.name
  location          = var.location
  capacity          = var.vmss_capacity
  tags              = var.tags
}
