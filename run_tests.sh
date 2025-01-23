#!/bin/bash

# 运行测试并生成覆盖率报告
pytest --cov=app --cov-report=html tests/

# 如果测试成功，显示覆盖率报告路径
if [ $? -eq 0 ]; then
    echo "测试完成！覆盖率报告已生成在 htmlcov/index.html"
fi 