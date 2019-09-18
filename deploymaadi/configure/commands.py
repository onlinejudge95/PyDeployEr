from click import echo, pass_context

from . import handlers
from ..cli import entry_point


@entry_point.command(
    help="Initializes the system by updating and upgrading the package manager."
)
@pass_context
def initialize(ctx):
    echo(f"Initializing configurations...")
    handlers.init(ctx, cfg=ctx.obj.get("CONFIG"))
    echo(f"Client initialized successfully!!")
