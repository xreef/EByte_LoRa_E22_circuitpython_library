import sys
sys.path.pop(0)
from setuptools import setup

setup(
    name="ebyte-lora-e22-circuitpython",
    package_dir={'': 'src'},
    py_modules=["lora_e22", "lora_e22_constants", "lora_e22_operation_constant"],
    version="0.0.1",
    description="CircuitPython LoRa EBYTE E22 device library complete and tested with Arduino SAMD, esp8266, esp32, Raspberry, rp2040 and STM32. sx1262/sx1268",
    long_description="CircuitPython Ebyte E22 LoRa (Long Range) library device very cheap and very long range (from 4Km to 10Km). LoRa EBYTE E22 device library complete and tested with  Arduino SAMD, esp8266, esp32 and STM32. sx1262/sx1268",
    keywords="LoRa, UART, EByte, esp32, esp8266, stm32, SAMD, Arduino, Raspberry Pi Pico, rp2040, CircuitPython,sx1262, sx1268, e22",
    url="https://github.com/xreef/EByte_LoRa_E22_circuitpython_library",
    author="Renzo Mischianti",
    author_email="renzo.mischianti@gmail.com",
    maintainer="Renzo Mischianti",
    maintainer_email="renzo.mischianti@gmail.com",
    license="MIT",
    install_requires=[],
    project_urls={
        'Documentation': 'https://www.mischianti.org/category/my-libraries/ebyte-lora-e22-devices/',
        'Documentazione': 'https://www.mischianti.org/it/category/le-mie-librerie/dispositivi-ebyte-lora-e22/',
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: Implementation",
        "License :: OSI Approved :: MIT License",
    ],
)
