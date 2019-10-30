import unittest
# Classes
import tests.test_cpf
import tests.test_cnh
import tests.test_cns
import tests.test_cnpj
import tests.test_titulo_eleitor


def suite():
    loader = unittest.TestLoader()
    test_suite = unittest.TestSuite()

    test_suite.addTests(loader.loadTestsFromModule(tests.test_cpf))
    test_suite.addTests(loader.loadTestsFromModule(tests.test_cnh))
    test_suite.addTests(loader.loadTestsFromModule(tests.test_cns))
    test_suite.addTests(loader.loadTestsFromModule(tests.test_cnpj))
    test_suite.addTests(loader.loadTestsFromModule(tests.test_titulo_eleitor))

    return test_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
