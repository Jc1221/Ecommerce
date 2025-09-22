@echo off
echo 运行测试并显示每个步骤的状态...
cd %~dp0
robot --outputdir results --loglevel DEBUG:INFO --console verbose EcommerceEndToEndTest.robot
pause