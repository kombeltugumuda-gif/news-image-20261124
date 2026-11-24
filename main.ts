// Entry program for the news-image-20261124 bounty (Node 22).
// It ships the finished front page as entry.png and copies it to the
// grader's output directory. No network, no randomness: the two grader
// runs write byte-identical files. The page itself was drawn ahead of
// time by build_frontpage.py around an AI illustration of the day's
// lead story (a Chinese court sentencing an official to death for
// leaking state secrets); this program only moves those bytes.
//
// Local check:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const here = dirname(fileURLToPath(import.meta.url));
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';

mkdirSync(outDir, { recursive: true });
copyFileSync(join(here, 'entry.png'), join(outDir, 'entry.png'));
