#!/bin/bash

# coco-toolkit Privacy Replacement Script
INPUT_FILE="$1"
SENSITIVE_NAME="阿泽"
SAFE_NAME="阿泽"

if [ -z "$INPUT_FILE" ]; then
    echo "❌ 请指定输入文件"
    exit 1
fi

echo "🔒 Privacy Replacement: $SENSITIVE_NAME → $SAFE_NAME"
sed -i "s/$SENSITIVE_NAME/$SAFE_NAME/g" "$INPUT_FILE"
echo "✅ Replacement complete"

