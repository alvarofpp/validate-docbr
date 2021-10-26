import unittest
# Classes
import tests.test_certidao
import tests.test_cpf
import tests.test_cnh
import tests.test_cns
import tests.test_cnpj
import tests.test_pis
import tests.test_renavam
import tests.test_titulo_eleitor
import tests.test_generic


def suite():
    loader = unittest.TestLoader()
    test_suite = unittest.TestSuite()

    test_suite.addTests(loader.loadTestsFromModule(tests.test_certidao))
    test_suite.addTests(loader.loadTestsFromModule(tests.test_cpf))
    test_suite.addTests(loader.loadTestsFromModule(tests.test_cnh))
    test_suite.addTests(loader.loadTestsFromModule(tests.test_cns))
    test_suite.addTests(loader.loadTestsFromModule(tests.test_cnpj))
    test_suite.addTests(loader.loadTestsFromModule(tests.test_pis))
    test_suite.addTests(loader.loadTestsFromModule(tests.test_renavam))
    test_suite.addTests(loader.loadTestsFromModule(tests.test_titulo_eleitor))
    test_suite.addTests(loader.loadTestsFromModule(tests.test_generic))

    return test_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
