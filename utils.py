import os

# Get system information
uname_info = os.uname()
specs = {
    "node_name": uname_info.nodename,
    "version": uname_info.version,
}

# Create opening_text using the provided specs
opening_text = f"Hello {specs['node_name']} user, nice to be on your {specs['version'] } machine."

