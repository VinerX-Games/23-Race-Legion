$ErrorActionPreference='Stop'
Add-Type -AssemblyName System.Drawing
$root='F:/Gemini_23Race'
$out="$root/art/interface/tooltip-background-preview"
New-Item -ItemType Directory -Force -Path "$out/previews" | Out-Null
$source=[System.Drawing.Bitmap]::new("$root/.cache/custom-ui-inputs/ToolTipBackground.png")
$dark=[System.Drawing.Bitmap]::new($source.Width,$source.Height)
for($y=0;$y -lt $source.Height;$y++){for($x=0;$x -lt $source.Width;$x++){
    $pixel=$source.GetPixel($x,$y)
    $dark.SetPixel($x,$y,[System.Drawing.Color]::FromArgb($pixel.A,8,8,8))
}}
$source.Save("$out/original.png",[System.Drawing.Imaging.ImageFormat]::Png)
$dark.Save("$out/human-tooltip-background.png",[System.Drawing.Imaging.ImageFormat]::Png)
$edge=[System.Drawing.Bitmap]::new("$root/.cache/custom-ui-inputs/ToolTipBorder.png")
function Patch($g,$image,$dx,$dy,$dw,$dh,$sx,$sy,$sw,$sh){
    $g.DrawImage($image,[System.Drawing.Rectangle]::new($dx,$dy,$dw,$dh),$sx,$sy,$sw,$sh,[System.Drawing.GraphicsUnit]::Pixel)
}
function Frame($background,$name,$w,$h,$b){
    $image=[System.Drawing.Bitmap]::new($w,$h)
    $g=[System.Drawing.Graphics]::FromImage($image)
    $brush=[System.Drawing.TextureBrush]::new($background)
    # The same FDF background insets and unchanged eight-section stock border.
    $g.FillRectangle($brush,2,2,($w-4),($h-4))
    $s=$edge.Height
    Patch $g $edge 0 $b $b ($h-2*$b) 0 0 $s $s
    Patch $g $edge ($w-$b) $b $b ($h-2*$b) $s 0 $s $s
    $top=$edge.Clone([System.Drawing.Rectangle]::new((2*$s),0,$s,$s),$edge.PixelFormat)
    $bottom=$edge.Clone([System.Drawing.Rectangle]::new((3*$s),0,$s,$s),$edge.PixelFormat)
    $top.RotateFlip([System.Drawing.RotateFlipType]::Rotate90FlipNone)
    $bottom.RotateFlip([System.Drawing.RotateFlipType]::Rotate90FlipNone)
    Patch $g $top $b 0 ($w-2*$b) $b 0 0 $s $s
    Patch $g $bottom $b ($h-$b) ($w-2*$b) $b 0 0 $s $s
    Patch $g $edge 0 0 $b $b (4*$s) 0 $s $s
    Patch $g $edge ($w-$b) 0 $b $b (5*$s) 0 $s $s
    Patch $g $edge 0 ($h-$b) $b $b (6*$s) 0 $s $s
    Patch $g $edge ($w-$b) ($h-$b) $b $b (7*$s) 0 $s $s
    $top.Dispose();$bottom.Dispose();$brush.Dispose();$g.Dispose()
    $image.Save("$out/previews/$name.png",[System.Drawing.Imaging.ImageFormat]::Png);$image.Dispose()
}
foreach($version in @('old','new')){
    $bg=if($version -eq 'old'){$source}else{$dark}
    Frame $bg "$version-welcome-panel" 512 512 12
    Frame $bg "$version-hud-board" 512 512 12
    Frame $bg "$version-tooltip" 512 256 9
    Frame $bg "$version-timer-chip" 512 64 7
}
$source.Dispose();$dark.Dispose();$edge.Dispose()
