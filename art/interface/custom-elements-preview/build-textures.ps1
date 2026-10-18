$ErrorActionPreference='Stop'
Add-Type -AssemblyName System.Drawing
$root='F:/Gemini_23Race'
$out="$root/art/interface/custom-elements-preview"
New-Item -ItemType Directory -Force -Path "$out/textures","$out/before" | Out-Null
$banner=[System.Drawing.Bitmap]::new("$root/art/interface/23raceforever-inventory-cover.png")
$chrome=[System.Drawing.Bitmap]::new("$root/.cache/custom-ui-inputs/MiniMapBorder.png")
$buttonChrome=[System.Drawing.Bitmap]::new("$root/.cache/custom-ui-inputs/ButtonBorder.png")
$stone=[System.Drawing.Bitmap]::new("$root/.cache/inventory-before.png")
$stockBg=[System.Drawing.Bitmap]::new("$root/.cache/custom-ui-inputs/ToolTipBackground.png")
$stockEdge=[System.Drawing.Bitmap]::new("$root/.cache/custom-ui-inputs/ToolTipBorder.png")
$stockButtonBg=[System.Drawing.Bitmap]::new("$root/.cache/custom-ui-inputs/EscMenuButtonBackground.png")
$stockButtonEdge=[System.Drawing.Bitmap]::new("$root/.cache/custom-ui-inputs/EscMenuButtonBorder.png")
$stockDownEdge=[System.Drawing.Bitmap]::new("$root/.cache/custom-ui-inputs/EscMenuButtonPushedBorder.png")
$stockDisabledBg=[System.Drawing.Bitmap]::new("$root/.cache/custom-ui-inputs/EscMenuButtonDisabledBackground.png")
$stockInputBg=[System.Drawing.Bitmap]::new("$root/.cache/custom-ui-inputs/EscMenuEditBoxBackground.png")
$stockInputEdge=[System.Drawing.Bitmap]::new("$root/.cache/custom-ui-inputs/EscMenuEditBoxBorder.png")
function Patch($g,$image,$dx,$dy,$dw,$dh,$sx,$sy,$sw,$sh) {
    if($dw -le 0 -or $dh -le 0){return}
    $g.DrawImage($image,[System.Drawing.Rectangle]::new($dx,$dy,$dw,$dh),$sx,$sy,$sw,$sh,[System.Drawing.GraphicsUnit]::Pixel)
}
function NineBorder($g,$image,$w,$h,$b,$s) {
    $iw=$image.Width;$ih=$image.Height
    Patch $g $image 0 0 $b $b 0 0 $s $s
    Patch $g $image ($w-$b) 0 $b $b ($iw-$s) 0 $s $s
    Patch $g $image 0 ($h-$b) $b $b 0 ($ih-$s) $s $s
    Patch $g $image ($w-$b) ($h-$b) $b $b ($iw-$s) ($ih-$s) $s $s
    Patch $g $image $b 0 ($w-2*$b) $b $s 0 ($iw-2*$s) $s
    Patch $g $image $b ($h-$b) ($w-2*$b) $b $s ($ih-$s) ($iw-2*$s) $s
    Patch $g $image 0 $b $b ($h-2*$b) 0 $s $s ($ih-2*$s)
    Patch $g $image ($w-$b) $b $b ($h-2*$b) ($iw-$s) $s $s ($ih-2*$s)
}
function StockBorder($g,$image,$w,$h,$b) {
    $s=$image.Height
    Patch $g $image 0 $b $b ($h-2*$b) 0 0 $s $s
    Patch $g $image ($w-$b) $b $b ($h-2*$b) $s 0 $s $s
    # Warcraft stores horizontal edge sections vertically and rotates them.
    $top=$image.Clone([System.Drawing.Rectangle]::new((2*$s),0,$s,$s),$image.PixelFormat)
    $bottom=$image.Clone([System.Drawing.Rectangle]::new((3*$s),0,$s,$s),$image.PixelFormat)
    $top.RotateFlip([System.Drawing.RotateFlipType]::Rotate90FlipNone)
    $bottom.RotateFlip([System.Drawing.RotateFlipType]::Rotate90FlipNone)
    Patch $g $top $b 0 ($w-2*$b) $b 0 0 $s $s
    Patch $g $bottom $b ($h-$b) ($w-2*$b) $b 0 0 $s $s
    $top.Dispose();$bottom.Dispose()
    Patch $g $image 0 0 $b $b (4*$s) 0 $s $s
    Patch $g $image ($w-$b) 0 $b $b (5*$s) 0 $s $s
    Patch $g $image 0 ($h-$b) $b $b (6*$s) 0 $s $s
    Patch $g $image ($w-$b) ($h-$b) $b $b (7*$s) 0 $s $s
}
function Cloth($w,$h,$brightness) {
    $im=[System.Drawing.Bitmap]::new($w,$h)
    $g=[System.Drawing.Graphics]::FromImage($im)
    $g.InterpolationMode=[System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
    # The plain fabric sample is above the logo, entirely inside the hem.
    Patch $g $banner 0 0 $w $h 222 514 182 124
    $g.Dispose()
    for($y=0;$y -lt $h;$y++) { for($x=0;$x -lt $w;$x++) {
        $c=$im.GetPixel($x,$y)
        $nx=($x-$w/2.0)/($w/2.0);$ny=($y-$h/2.0)/($h/2.0)
        $v=$brightness*(1.0-0.13*[Math]::Min(1.0,($nx*$nx+$ny*$ny)/2))
        $im.SetPixel($x,$y,[System.Drawing.Color]::FromArgb(255,[int]($c.R*$v),[int]($c.G*$v),[int]($c.B*$v)))
    }}
    return ,$im
}
function Save($im,$name,$folder='textures') {
    $im.Save("$out/$folder/$name.png",[System.Drawing.Imaging.ImageFormat]::Png)
    $im.Dispose()
}
function Panel($name,$w,$h,$brightness,$border,$stoneTop=$false) {
    $im=Cloth $w $h $brightness
    $g=[System.Drawing.Graphics]::FromImage($im)
    $g.InterpolationMode=[System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
    NineBorder $g $chrome $w $h $border 16
    if($stoneTop){Patch $g $stone $border 0 ($w-2*$border) 13 5 461 450 27}
    $g.Dispose();Save $im $name
    $old=[System.Drawing.Bitmap]::new($w,$h)
    $g=[System.Drawing.Graphics]::FromImage($old)
    $brush=[System.Drawing.TextureBrush]::new($stockBg)
    $g.FillRectangle($brush,0,0,$w,$h)
    StockBorder $g $stockEdge $w $h ([Math]::Min(12,$border))
    $brush.Dispose();$g.Dispose();Save $old $name 'before'
}
Panel 'hud-board' 512 512 0.19 12 $true
Panel 'timer-chip' 512 64 0.23 7
Panel 'tooltip' 512 256 0.14 9
Panel 'welcome-panel' 512 512 0.22 14 $true
Panel 'editbox' 512 64 0.10 7
foreach($state in @('normal','hover','pressed','disabled')) {
    $brightness=switch($state){'normal'{0.34}'hover'{0.48}'pressed'{0.18}'disabled'{0.17}}
    $im=Cloth 256 64 $brightness
    $g=[System.Drawing.Graphics]::FromImage($im)
    NineBorder $g $buttonChrome 256 64 10 12
    if($state -eq 'hover') {
        $pen=[System.Drawing.Pen]::new([System.Drawing.Color]::FromArgb(130,235,197,108),2)
        $g.DrawRectangle($pen,3,3,249,57);$pen.Dispose()
    }
    if($state -eq 'pressed') {
        $pen=[System.Drawing.Pen]::new([System.Drawing.Color]::FromArgb(190,0,0,0),4)
        $g.DrawRectangle($pen,5,5,245,53);$pen.Dispose()
    }
    $g.Dispose()
    if($state -eq 'disabled') {
        for($y=0;$y -lt 64;$y++){for($x=0;$x -lt 256;$x++){
            $c=$im.GetPixel($x,$y);$l=[int](($c.R*0.3+$c.G*0.59+$c.B*0.11)*0.65)
            $im.SetPixel($x,$y,[System.Drawing.Color]::FromArgb($c.A,$l,$l,$l))
        }}
    }
    Save $im "button-$state"
    $old=[System.Drawing.Bitmap]::new(256,64);$g=[System.Drawing.Graphics]::FromImage($old)
    $bg=if($state -eq 'disabled'){$stockDisabledBg}else{$stockButtonBg}
    $brush=[System.Drawing.TextureBrush]::new($bg);$g.FillRectangle($brush,0,0,256,64)
    $edge=if($state -eq 'pressed'){$stockDownEdge}else{$stockButtonEdge}
    StockBorder $g $edge 256 64 16
    if($state -eq 'hover'){$pen=[System.Drawing.Pen]::new([System.Drawing.Color]::FromArgb(110,255,220,100),2);$g.DrawRectangle($pen,3,3,249,57);$pen.Dispose()}
    $brush.Dispose();$g.Dispose();Save $old "button-$state" 'before'
}
# The actual editbox uses its own standard stock material, not the tooltip.
$old=[System.Drawing.Bitmap]::new(512,64);$g=[System.Drawing.Graphics]::FromImage($old)
$brush=[System.Drawing.TextureBrush]::new($stockInputBg);$g.FillRectangle($brush,0,0,512,64)
StockBorder $g $stockInputEdge 512 64 16
$brush.Dispose();$g.Dispose();Save $old 'editbox' 'before'
$im=Cloth 64 64 0.30;$g=[System.Drawing.Graphics]::FromImage($im)
NineBorder $g $buttonChrome 64 64 10 12;$g.Dispose();Save $im 'toggle'
Save ([System.Drawing.Bitmap]::new($buttonChrome)) 'toggle' 'before'
$im=Cloth 512 32 0.30;Save $im 'row-stripe'
$im=[System.Drawing.Bitmap]::new(512,32);$g=[System.Drawing.Graphics]::FromImage($im)
$g.Clear([System.Drawing.Color]::FromArgb(14,255,255,255));$g.Dispose();Save $im 'row-stripe' 'before'
$im=[System.Drawing.Bitmap]::new(512,8);$g=[System.Drawing.Graphics]::FromImage($im)
Patch $g $chrome 0 0 512 8 16 0 480 16;$g.Dispose();Save $im 'separator'
$im=[System.Drawing.Bitmap]::new(512,8);$g=[System.Drawing.Graphics]::FromImage($im)
$g.Clear([System.Drawing.Color]::FromArgb(35,255,255,255));$g.Dispose();Save $im 'separator' 'before'
Save (Cloth 256 256 0.19) 'panel-background'
# A Warcraft-compatible eight-cell edge strip, assembled from the custom frame.
$strip=[System.Drawing.Bitmap]::new(128,16);$g=[System.Drawing.Graphics]::FromImage($strip)
$rects=@(@(0,16,16,480),@(496,16,16,480),@(16,0,480,16),@(16,496,480,16),@(0,0,16,16),@(496,0,16,16),@(0,496,16,16),@(496,496,16,16))
for($i=0;$i -lt 8;$i++){
    $r=$rects[$i]
    if($i -eq 2 -or $i -eq 3){
        $tile=[System.Drawing.Bitmap]::new(16,16);$tg=[System.Drawing.Graphics]::FromImage($tile)
        Patch $tg $chrome 0 0 16 16 $r[0] $r[1] $r[2] $r[3];$tg.Dispose()
        $tile.RotateFlip([System.Drawing.RotateFlipType]::Rotate270FlipNone)
        Patch $g $tile ($i*16) 0 16 16 0 0 16 16;$tile.Dispose()
    } else { Patch $g $chrome ($i*16) 0 16 16 $r[0] $r[1] $r[2] $r[3] }
}
$g.Dispose();Save $strip 'panel-edge'
$banner.Dispose();$chrome.Dispose();$buttonChrome.Dispose();$stone.Dispose();$stockBg.Dispose();$stockEdge.Dispose();$stockButtonBg.Dispose();$stockButtonEdge.Dispose();$stockDownEdge.Dispose();$stockDisabledBg.Dispose();$stockInputBg.Dispose();$stockInputEdge.Dispose()
Write-Output 'Prepared custom UI textures outside map.w3x.'
