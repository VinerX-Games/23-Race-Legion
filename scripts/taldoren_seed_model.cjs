// Модель куста Семени Тал'дорена (war3mapImported/TalDorenSeed.mdx). Нужен war3-model из MDLxL.
// Исходник — doodads\ashenvale\plants\ashenbush0\ashenbush0.mdx из CASC (SD).
// node scripts/taldoren_seed_model.cjs <ashenbush0.mdx> map.w3x/war3mapImported/TalDorenSeed.mdx
// AshenBush0 (SD) + последовательность Death: куст оседает, сжимается к земле и тает за 1.2 сек.
const {readMdx, writeMdx}=require('C:/Users/oleg7/.claude/skills/model-set-prep/scripts/common.cjs');
const [src, dst] = process.argv.slice(2);
const m = readMdx(src);
const LINEAR = 1, D0 = 3100, D1 = 4300;
const v3 = (x, y, z) => Float32Array.from([x, y, z]);
const ext = { BoundsRadius: m.Info.BoundsRadius, MinimumExtent: Float32Array.from(m.Info.MinimumExtent), MaximumExtent: Float32Array.from(m.Info.MaximumExtent) };
m.Sequences.forEach(s => Object.assign(s, ext));
m.Sequences.push({ Name: 'Death', Interval: Uint32Array.from([D0, D1]), MoveSpeed: 0, NonLooping: true, Rarity: 0, ...ext });
m.Bones[0].Scaling = { LineType: LINEAR, GlobalSeqId: null, Keys: [
  { Frame: 0, Vector: v3(1, 1, 1) }, { Frame: 3000, Vector: v3(1, 1, 1) },
  { Frame: D0, Vector: v3(1, 1, 1) }, { Frame: 3500, Vector: v3(1.1, 1.1, 0.8) },
  { Frame: 3900, Vector: v3(0.6, 0.6, 0.35) }, { Frame: D1, Vector: v3(0.02, 0.02, 0.02) },
] };
m.GeosetAnims = [{ GeosetId: 0, Flags: 0, Color: v3(1, 1, 1), Alpha: { LineType: LINEAR, GlobalSeqId: null, Keys: [
  { Frame: 0, Vector: Float32Array.from([1]) }, { Frame: 3000, Vector: Float32Array.from([1]) },
  { Frame: D0, Vector: Float32Array.from([1]) }, { Frame: 3800, Vector: Float32Array.from([0.9]) },
  { Frame: D1, Vector: Float32Array.from([0]) },
] } }];
m.Bones[0].GeosetAnimId = 0;
m.Info.Name = 'TalDorenSeed';
writeMdx(dst, m);
const r = readMdx(dst);
console.log(r.Sequences.map(s => s.Name + ' ' + Array.from(s.Interval) + (s.NonLooping ? ' once' : ' loop')).join(' | '),
  '| scale keys', r.Bones[0].Scaling.Keys.length, '| alpha keys', r.GeosetAnims[0].Alpha.Keys.length);
