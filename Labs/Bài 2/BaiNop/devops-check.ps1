$ErrorActionPreference = 'Stop'
Write-Output '=== DEVOPS TOOLCHAIN CHECK ==='
foreach ($tool in 'code','git','docker','node') {
    if (-not (Get-Command $tool -ErrorAction SilentlyContinue)) { throw "Missing tool: $tool" }
    $result = & $tool --version
    if ($LASTEXITCODE -ne 0) { throw "Version check failed: $tool" }
    Write-Output ("{0}: {1}" -f $tool, ($result | Select-Object -First 1))
}
docker info --format 'Docker Engine: {{.ServerVersion}} / {{.OSType}}'
if ($LASTEXITCODE -ne 0) { throw 'Docker Engine is unavailable' }
Write-Output 'Required toolchain is ready.'
