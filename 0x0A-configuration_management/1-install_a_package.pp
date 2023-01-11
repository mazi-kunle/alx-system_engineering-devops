# install flask from pip3 with puppet

package {'flask':
  ensure   => installed,
  provider => pip3
}
