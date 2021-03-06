#!/usr/bin/env python
# Eclipse SUMO, Simulation of Urban MObility; see https://eclipse.org/sumo
# Copyright (C) 2009-2018 German Aerospace Center (DLR) and others.
# This program and the accompanying materials
# are made available under the terms of the Eclipse Public License v2.0
# which accompanies this distribution, and is available at
# http://www.eclipse.org/legal/epl-v20.html
# SPDX-License-Identifier: EPL-2.0

# @file    test.py
# @author  Pablo Alvarez Lopez
# @date    2016-11-25
# @version $Id$

# import common functions for netedit tests
import os
import sys

testRoot = os.path.join(os.environ.get('SUMO_HOME', '.'), 'tests')
neteditTestRoot = os.path.join(
    os.environ.get('TEXTTEST_HOME', testRoot), 'netedit')
sys.path.append(neteditTestRoot)
import neteditTestFunctions as netedit  # noqa

# Open netedit
neteditProcess, referencePosition = netedit.setupAndStart(neteditTestRoot)

# Rebuild network
netedit.rebuildNetwork()

# show connections
netedit.toogleShowConnectionsInspectorMode()

# go to select mode
netedit.selectMode()

# select connection
netedit.leftClick(referencePosition, 250, 125)
netedit.leftClick(referencePosition, 250, 190)
netedit.leftClick(referencePosition, 250, 257)
netedit.leftClick(referencePosition, 250, 325)

# go to inspect mode agaim
netedit.inspectMode()

# inspect selected connection
netedit.leftClick(referencePosition, 250, 125)

# Change generic parameters with a dummy value
netedit.modifyAttribute(7, "dummyGenericParameters")

# Change generic parameters with a invalid format
netedit.modifyAttribute(7, "key1|key2|key3")

# Change generic parameters with a valid value
netedit.modifyAttribute(7, "key1=value1|key2=value2|key3=value3")

# Change generic parameters with a valid value (empty values)
netedit.modifyAttribute(7, "key1=|key2=|key3=")

# Change generic parameters with a valid value (all empty)
netedit.modifyAttribute(7, "")

# Change generic parameters with an invalid value (duplicated)
netedit.modifyAttribute(7, "key1duplicated=value1|key1duplicated=value2|key3=value3")

# Change generic parameters with a valid value
netedit.modifyAttribute(7, "key1=valueDuplicated|key2=valueDuplicated|key3=valueDuplicated")

# Change generic parameters with an invalid value (invalid key characters)
netedit.modifyAttribute(7, "keyInvalid.;%>%$$=value1|key2=value2|key3=value3")

# Change generic parameters with a invalid value (invalid value characters)
netedit.modifyAttribute(7, "key1=valueInvalid%;%$<>$$%|key2=value2|key3=value3")

# Change generic parameters with a valid value
netedit.modifyAttribute(7, "keyFinal1=value1|keyFinal2=value2|keyFinal3=value3")

# Check undo redo
netedit.undo(referencePosition, 7)
netedit.rebuildNetwork()
netedit.redo(referencePosition, 7)

# save network
netedit.saveNetwork()

# quit netedit
netedit.quit(neteditProcess)
