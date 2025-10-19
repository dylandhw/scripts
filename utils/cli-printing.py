from rich.console import Console
from rich.panel import Panel
from rich.columns import Columns

console = Console()
panel = Panel(
    "[bold blue]test[/bold blue]",
    title="[green]System[/green]",
    subtitle="[yellow]v1.0[/yellow]",
    border_style="bright_blue",
    expand=False
)
console.print(panel)

panels = [
    Panel("panel 1 content", title="Box 1"),
    Panel("panel 2 content", title="Box 2"),
    Panel("panel 3 content", title="Box 3")
]
console.print(Columns(panels))
