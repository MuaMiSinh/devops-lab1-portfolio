param([string]$ProjectPath = (Join-Path $PSScriptRoot 'dev-env'))
$ErrorActionPreference = 'Stop'
$timer = [Diagnostics.Stopwatch]::StartNew()
foreach ($tool in 'git','node','npm.cmd') {
    if (-not (Get-Command $tool -ErrorAction SilentlyContinue)) { throw "Missing prerequisite: $tool" }
}
Write-Output '[1/4] Prerequisites ready'
New-Item -ItemType Directory -Force -Path $ProjectPath | Out-Null
foreach ($folder in 'src','tests','docs') {
    New-Item -ItemType Directory -Force -Path (Join-Path $ProjectPath $folder) | Out-Null
}
Write-Output '[2/4] Created src/ tests/ docs/'
foreach ($name in 'server.js','package.json') {
    $target = Join-Path $ProjectPath $name
    if (-not (Test-Path -LiteralPath $target)) { Copy-Item -LiteralPath (Join-Path $PSScriptRoot $name) -Destination $target }
}
$ignore = Join-Path $ProjectPath '.gitignore'
if (-not (Test-Path -LiteralPath $ignore)) { "node_modules/`n.env`n*.log`ndist/" | Set-Content -LiteralPath $ignore -Encoding utf8 }
$readme = Join-Path $ProjectPath 'README.md'
if (-not (Test-Path -LiteralPath $readme)) { "# Lab 2 automation demo`nRun: npm start`nDirectories: src, tests, docs" | Set-Content -LiteralPath $readme -Encoding utf8 }
Write-Output '[3/4] Generated application and configuration (existing files preserved)'
Push-Location -LiteralPath $ProjectPath
try {
    npm.cmd install --ignore-scripts --no-audit --no-fund
    if ($LASTEXITCODE -ne 0) { throw 'npm install failed' }
} finally { Pop-Location }
Write-Output '[4/4] Dependencies ready'
$timer.Stop()
Write-Output ('SETUP COMPLETE in {0:N2}s: {1}' -f $timer.Elapsed.TotalSeconds, $ProjectPath)
Write-Output 'Source control: project is inside the course repository; no nested git repository created.'
