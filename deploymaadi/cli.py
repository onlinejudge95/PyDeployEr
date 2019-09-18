import json
import pathlib

from click import group, pass_context


@group()
@pass_context
def entry_point(ctx):
    ctx.ensure_object(dict)

    config_file_path = pathlib.Path.cwd() / "etc" / "config.json"
    with config_file_path.open(mode="r") as fp:
        config_object = json.load(fp)

    ctx.obj["CONFIG"] = config_object


from .configure import commands as configure

entry_point.add_command(configure.initialize)
