Lossh
---
Share localhost through SSH. Making local/remote port forwarding easy and safe.

Installation
---
Works with both Python 3+ and Python 2.7+ versions:
```
pip install lossh
```

Functionality
---
```
# cast your localhost to someone else
lossh cast RECEIVER

# No need to keep a terminal open
lossh listen SENDER --background

# Kills a `lossh listen` in the background
lossh kill [optional: PORT, default=52222]

# Remove all settings for a user (by default lossh0).
lossh remove_user

# View how you can be accessed
lossh ls # outputs
user="lossh0" port=52222 ssh_key=AAAAB3NzaC ..... joCyayMg+d account="saumil@SaumilPC"

# Create specific user+port combination (don't forget to share this info with buddy)
# And don't forget the quotes
lossh create "PUBKEY" lossh5@someip --port 5000

# NOTE: default is to serve at 52222, so can be viewed at 52222
lossh listen lossh5@someip --remote_port 5000

# Now receiver can locally view at 5000
lossh listen lossh5@someip --remote_port 5000 --local_port 5000

# push your content to someone who created a lossh user for you
lossh cast lossh5@someip --remote_port 5000 --local_port 5000

# Expose will open beyond the machine (serving on 0.0.0.0 and not localhost)
lossh listen lossh5@someip --expose
```
