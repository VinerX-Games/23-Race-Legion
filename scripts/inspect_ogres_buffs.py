# -*- coding: utf-8 -*-
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wc3_hivewe as hw
from inspect_race_base import inspect_buff

for bid in ['B083', 'B097', 'B098', 'B081', 'BUfa', 'BUts', 'Bspl', 'Bliq', 'Bblo', 'Bfzy', 'Blsh', 'B05G', 'B07V', 'B07W', 'B07X', 'B07Y', 'B07Z', 'B080']:
    b = inspect_buff(bid)
    print(f"Buff {bid}: editorname='{b.get('editorname')}' tip='{b.get('bufftip')}' ub='{b.get('buffubertip')}' (raw_tip={b.get('raw_bufftip')}, raw_ub={b.get('raw_buffubertip')})")
