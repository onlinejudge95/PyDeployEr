from click import echo
from fabric import Connection


def init(ctx, cfg=None):
    if not cfg:
        raise ValueError("No config set, provide a config file.")

    host = cfg.get("host")
    user = cfg.get("user")
    echo(f"Connecting to {user} @ {host}")
    conn = Connection(host, user=user)

    conn.sudo("apt-get -y update")
    conn.sudo("apt-get -y upgrade")
