from src.stages.contracts.mocks.extract_contractMock import extract_contract_mock
from src.stages.contracts.tranform_contract import TranformContract
from src.errors.transform_error import TransformError
from .transform_raw_data import TransformRawData


def test_transform():
    transform_raw_data = TransformRawData()
    transformed_data_contract = transform_raw_data.transform(extract_contract_mock)

    assert isinstance(transformed_data_contract, TranformContract)
    assert "first_name" in transformed_data_contract.load_content[0]
    assert "second_name" in transformed_data_contract.load_content[0]
    assert "artist_id" in transformed_data_contract.load_content[0]
    assert "link" in transformed_data_contract.load_content[0]
    assert "extraction_date" in transformed_data_contract.load_content[0]

def test_transform_error():
    transform_raw_data = TransformRawData()
    try:
        transform_raw_data.transform('entradaerrada')
    except Exception as exception: # pylint: disable=broad=except
        assert isinstance(exception, TransformError)
