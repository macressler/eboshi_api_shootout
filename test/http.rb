require "net/http"
require "json"

class Request < Struct.new(:method, :url, :data)
  def self.get url
    new(:get, url).tap(&:call)
  end

  def self.post url, data=nil
    new(:get, url, data).tap(&:call)
  end

  attr_accessor :response

  def call
    self.response = Net::HTTP.new("localhost", 6969).start do |http|
      request = Net::HTTP.const_get(method.to_s.capitalize).new(url, 'Content-Type' =>'application/json')
      request.body = JSON.dump(data) if data
      http.request(request)
    end
  end

  def body
    return unless response
    JSON.load(response.body)
  rescue JSON::ParserError
    response.body
  end
end

