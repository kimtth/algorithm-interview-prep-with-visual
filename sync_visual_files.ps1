# Sync visual files from section directories to root visual folder
# Keep the newest version of each file

$rootVisual = "d:\Code\algorithm-interview-with-visual\visual"
$sectionDirs = @(
    "d:\Code\algorithm-interview-with-visual\2-python\ch06\visual",
    "d:\Code\algorithm-interview-with-visual\3-linear-data-structures\ch07\visual",
    "d:\Code\algorithm-interview-with-visual\3-linear-data-structures\ch08\visual",
    "d:\Code\algorithm-interview-with-visual\3-linear-data-structures\ch09\visual",
    "d:\Code\algorithm-interview-with-visual\3-linear-data-structures\ch10\visual",
    "d:\Code\algorithm-interview-with-visual\3-linear-data-structures\ch11\visual",
    "d:\Code\algorithm-interview-with-visual\4-non-linear-data-structures\ch12\visual",
    "d:\Code\algorithm-interview-with-visual\4-non-linear-data-structures\ch13\visual",
    "d:\Code\algorithm-interview-with-visual\4-non-linear-data-structures\ch14\visual",
    "d:\Code\algorithm-interview-with-visual\4-non-linear-data-structures\ch15\visual",
    "d:\Code\algorithm-interview-with-visual\4-non-linear-data-structures\ch16\visual",
    "d:\Code\algorithm-interview-with-visual\5-algorithms\ch17\visual",
    "d:\Code\algorithm-interview-with-visual\5-algorithms\ch18\visual",
    "d:\Code\algorithm-interview-with-visual\5-algorithms\ch19\visual",
    "d:\Code\algorithm-interview-with-visual\5-algorithms\ch20\visual",
    "d:\Code\algorithm-interview-with-visual\5-algorithms\ch21\visual",
    "d:\Code\algorithm-interview-with-visual\5-algorithms\ch22\visual",
    "d:\Code\algorithm-interview-with-visual\5-algorithms\ch23\visual"
)

Write-Host "Starting visual files sync..." -ForegroundColor Cyan
Write-Host ""

$copiedCount = 0
$skippedCount = 0
$newerInRootCount = 0

# Step 1: Find all HTML files in section visual directories
foreach ($sectionDir in $sectionDirs) {
    if (-not (Test-Path $sectionDir)) {
        continue
    }
    
    $htmlFiles = Get-ChildItem -Path $sectionDir -Filter "*.html" -ErrorAction SilentlyContinue
    
    foreach ($file in $htmlFiles) {
        $fileName = $file.Name
        $rootFile = Join-Path $rootVisual $fileName
        
        # Check if file exists in root visual
        if (Test-Path $rootFile) {
            $sectionLastWrite = $file.LastWriteTime
            $rootLastWrite = (Get-Item $rootFile).LastWriteTime
            
            if ($sectionLastWrite -gt $rootLastWrite) {
                # Section file is newer, copy it
                Copy-Item $file.FullName $rootFile -Force
                Write-Host "[UPDATED] $fileName (section newer: $sectionLastWrite)" -ForegroundColor Green
                $copiedCount++
            } else {
                # Root file is same or newer, skip
                Write-Host "[SKIP] $fileName (root is current: $rootLastWrite)" -ForegroundColor Yellow
                $newerInRootCount++
            }
        } else {
            # File doesn't exist in root, copy it
            Copy-Item $file.FullName $rootFile -Force
            Write-Host "[NEW] $fileName" -ForegroundColor Cyan
            $copiedCount++
        }
    }
}

Write-Host ""
Write-Host "Sync completed!" -ForegroundColor Green
Write-Host "  - Copied/Updated: $copiedCount files" -ForegroundColor Green
Write-Host "  - Skipped (root current): $newerInRootCount files" -ForegroundColor Yellow
Write-Host ""

# Step 2: Ask user before deleting section visual directories
Write-Host "Do you want to remove all HTML files from section visual directories? (y/n): " -ForegroundColor Yellow -NoNewline
$confirmation = Read-Host

if ($confirmation -eq 'y' -or $confirmation -eq 'Y') {
    Write-Host ""
    Write-Host "Removing HTML files from section directories..." -ForegroundColor Cyan
    
    $deletedCount = 0
    
    foreach ($sectionDir in $sectionDirs) {
        if (-not (Test-Path $sectionDir)) {
            continue
        }
        
        $htmlFiles = Get-ChildItem -Path $sectionDir -Filter "*.html" -ErrorAction SilentlyContinue
        
        foreach ($file in $htmlFiles) {
            Remove-Item $file.FullName -Force
            Write-Host "[DELETED] $($file.FullName)" -ForegroundColor Red
            $deletedCount++
        }
    }
    
    Write-Host ""
    Write-Host "Cleanup completed! Deleted $deletedCount HTML files from section directories." -ForegroundColor Green
} else {
    Write-Host "Cleanup cancelled. Section files remain unchanged." -ForegroundColor Yellow
}

Write-Host ""
Write-Host "Done!" -ForegroundColor Cyan
