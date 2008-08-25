#!/usr/bin/ruby
require "test/unit"

# Setup our library paths properly so we can be called by make
# or by hand.
if ENV['PWD'] =~ /.*tests.*/
	$:.insert(0, "#{ENV['PWD']}/../ruby/")
else
	$:.insert(0, "#{ENV['PWD']}/ruby/")
end
# imports to test
require "thwap/core/config"

def _callback
	return 1
end

# libTHWAP unit tests
class UnitTest < Test::Unit::TestCase
	def test_slurp
		@thSlurpFlag = 0
		fp = File.open('/tmp/thwap', 'w+')
		fp.write("this is a test\nbut this is not")
		fp.close
		fp = File.open('/tmp/thwap', 'r')
		thSlurp = THWAP::Config::ThSlurp.new()
		thSlurp.send :registerTrigger, '^this.*', _callback
		thSlurp.send :process, fp
		assert_equal(0, @thSlurpFlag)
	end

	def test_config
		assert_equal(0, 0)
	end

	def test_threadpools
		obj = nil
	end
end
