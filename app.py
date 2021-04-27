#!/usr/bin/env python
import os
from permissions import Permissions
# import requests  # noqa We are just importing this to prove the dependency installed correctly


# Parse the permissions file
lobPermissions = Permissions()
lobPermissionData= lobPermissions.parseYML("/github/workspace/" + os.environ['permissions_file_path'])
# permissions = lobPermissions.parseYML('test.yml')

# Parse the permissions file
trimisPermission = Permissions()
trimisPermissionData = trimisPermission.parseYML("/github/workspace/" + os.environ['restrictions_file_path'])
    
print(f"::set-output name=lob::{lobPermissionData}")
print(f"::set-output name=trimis::{trimisPermissionData}")


# if __name__ == "__main__":
#     main()