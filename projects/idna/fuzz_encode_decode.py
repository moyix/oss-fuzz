#!/usr/bin/python3
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import sys
import atheris

import idna


def TestOneInput(data):
    """Fuzz encode and decode"""
    fdp = atheris.FuzzedDataProvider(data)
    try:
        idna.encode(fdp.ConsumeString(1024))
    except idna.IDNAError:
        pass
    
    try:
        idna.decode(fdp.ConsumeString(1024))
    except idna.IDNAError:
        pass


def main():
    atheris.instrument_all()
    atheris.Setup(sys.argv, TestOneInput, enable_python_coverage=True)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
