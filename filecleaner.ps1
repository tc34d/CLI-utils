param(
    [string]$Path = "$env:TEMP"
)

Get-ChildItem -Path $Path -Filter "*.tmp" | Remove-Item -Force
