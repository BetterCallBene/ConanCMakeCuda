from conans import ConanFile, CMake, tools


class ParticleConan(ConanFile):
    name = "particle"
    version = "0.1.0"
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Particle here>"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    exports_sources=["src/"]

    def build(self):
        cmake = CMake(self)
        cmake.definitions["CMAKE_CUDA_FLAGS"] = "-arch=compute_53"
        cmake.configure()
        cmake.build()
        cmake.test()

    def package_info(self):
        self.cpp_info.libs = ["hello"]

