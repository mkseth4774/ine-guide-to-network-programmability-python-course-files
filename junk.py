##
##

import subnetmod1

network = input('Please enter a subnet and mask in the form "10.0.0.0/18":')

subnetmod1.broadcast_address(network)
subnetmod1.netmask(network)
subnetmod1.wildcard_mask(network)
subnetmod1.hostips(network)
subnetmod1.firsthostip(network)
subnetmod1.lasthostip(network)

##
## End of file...
