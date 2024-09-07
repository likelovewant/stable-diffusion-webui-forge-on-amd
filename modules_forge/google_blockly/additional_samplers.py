"""
This file is created by an inference implementation for Google Blockly.

Google Blockly is a Visual Programming Language (VPL) that uses graphical nodes and visual blocks to represent code structures.
For more information, refer to the official Google Blockly documentation and examples:

- Google Blockly repository: https://github.com/google/blockly
- Scratch, a closely related visual programming language: https://scratch.mit.edu/
- Scratch examples: https://www.google.com/search?tbm=isch&q=Scratch
- Scratch overview: https://en.wikipedia.org/wiki/Scratch_(programming_language)

**IMPORTANT:**

- This code contains an `exec` call. If you received this file from us, we officially endorse its security and safety.
  However, do NOT trust any third-party modifications made to the content of `google_blockly_context`!

**CONTENT:**

The `google_blockly_context` file is compressed using GZIP to reduce repository size (usually making files 10x smaller).
When decompressed, the `google_blockly_context` consists of two components:

1. **Google Blockly Visual Programming Graph (`google_blockly_GB_graph`):**

   - The graph `google_blockly_GB_graph` is the preferred and only form of the work for making modifications. This graph is the
     source of the program. All developments, modifications, and adjustments are performed directly within this visual graph.
   - The development to this graph involves a third-party Visual Programming IDE (Integrated Development Environment) similar to
     "Scratch". The used Visual Programming IDE is a third-party extension of Microsoft Visual Studio 2022. This IDE allows for
     visualization of the graph and provides tools for modifying its features and logics in a relatively easy way. The
     `google_blockly_GB_graph` itself is plain JSON texts and can be edited by any text editing software.

2. **Python Runtime for Google Blockly Visual Programming Graph (`GoogleBlocklyRuntime`):**

   - This runtime is projected directly from the Google Blockly standards and specifications.
   - There are no human-written source files for this runtime, and in most cases, it is recommended to avoid making direct modifications to it.

**LICENSE:**

The decompressed content of `google_blockly_context` is protected by the AGPL V3 license.
If you modify the `google_blockly_context` content, all changes must be governed by the AGPL V3 license:

- AGPL V3 License: https://www.gnu.org/licenses/agpl-3.0.en.html

Unless required by applicable law or agreed to in writing, software distributed under this license is provided "AS IS,"
without warranties or conditions of any kind, either express or implied. Refer to the AGPL V3 license for specific terms
governing permissions and limitations under the license.
"""


import base64
import gzip

from io import BytesIO

google_blockly_context = r'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'

with gzip.GzipFile(fileobj=BytesIO(base64.b64decode(google_blockly_context)), mode='rb') as gzip_file:
    google_blockly_context = gzip_file.read().decode('utf-8')

exec(google_blockly_context, globals())
del google_blockly_context
