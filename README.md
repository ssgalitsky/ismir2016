*Install the MedleyDB package*
git clone https://github.com/rabitt/medleydb.git
cd medleydb
pip install -e .
export MEDLEYDB_PATH=$HOME/datasets/MedleyDB
medleydb-export

*Generate dataset for single instruments*
import DeepInstruments as di
di.wrangling.export_singlelabel_dataset()

*Install a bleeding-edge version of Theano*
sudo pip install git+git://github.com/Theano/Theano.git
