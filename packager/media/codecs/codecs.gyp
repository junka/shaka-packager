# Copyright 2014 Google Inc. All rights reserved.
#
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file or at
# https://developers.google.com/open-source/licenses/bsd

{
  'variables': {
    'shaka_code': 1,
  },
  'targets': [
    {
      'target_name': 'codecs',
      'type': '<(component)',
      'sources': [
        'aac_audio_specific_config.cc',
        'aac_audio_specific_config.h',
        'ac3_audio_util.cc',
        'ac3_audio_util.h',
        'av1_codec_configuration_record.cc',
        'av1_codec_configuration_record.h',
        'av1_parser.cc',
        'av1_parser.h',
        'avc_decoder_configuration_record.cc',
        'avc_decoder_configuration_record.h',
        'decoder_configuration_record.cc',
        'decoder_configuration_record.h',
        'ec3_audio_util.cc',
        'ec3_audio_util.h',
        'es_descriptor.cc',
        'es_descriptor.h',
        'h264_byte_to_unit_stream_converter.cc',
        'h264_byte_to_unit_stream_converter.h',
        'h264_parser.cc',
        'h264_parser.h',
        'h265_byte_to_unit_stream_converter.cc',
        'h265_byte_to_unit_stream_converter.h',
        'h265_parser.cc',
        'h265_parser.h',
        'h26x_bit_reader.cc',
        'h26x_bit_reader.h',
        'h26x_byte_to_unit_stream_converter.cc',
        'h26x_byte_to_unit_stream_converter.h',
        'hevc_decoder_configuration_record.cc',
        'hevc_decoder_configuration_record.h',
        'hls_audio_util.cc',
        'hls_audio_util.h',
        'nal_unit_to_byte_stream_converter.cc',
        'nal_unit_to_byte_stream_converter.h',
        'nalu_reader.cc',
        'nalu_reader.h',
        'video_slice_header_parser.cc',
        'video_slice_header_parser.h',
        'vp_codec_configuration_record.cc',
        'vp_codec_configuration_record.h',
        'vp8_parser.cc',
        'vp8_parser.h',
        'vp9_parser.cc',
        'vp9_parser.h',
        'vpx_parser.h',
      ],
      'dependencies': [
        '../../base/base.gyp:base',
        '../../third_party/gflags/gflags.gyp:gflags',
      ],
    },
    {
      'target_name': 'codecs_unittest',
      'type': '<(gtest_target_type)',
      'sources': [
        'aac_audio_specific_config_unittest.cc',
        'ac3_audio_util_unittest.cc',
        'av1_codec_configuration_record_unittest.cc',
        'av1_parser_unittest.cc',
        'avc_decoder_configuration_record_unittest.cc',
        'ec3_audio_util_unittest.cc',
        'es_descriptor_unittest.cc',
        'h264_byte_to_unit_stream_converter_unittest.cc',
        'h264_parser_unittest.cc',
        'h265_byte_to_unit_stream_converter_unittest.cc',
        'h265_parser_unittest.cc',
        'h26x_bit_reader_unittest.cc',
        'hevc_decoder_configuration_record_unittest.cc',
        'hls_audio_util_unittest.cc',
        'nal_unit_to_byte_stream_converter_unittest.cc',
        'nalu_reader_unittest.cc',
        'video_slice_header_parser_unittest.cc',
        'vp_codec_configuration_record_unittest.cc',
        'vp8_parser_unittest.cc',
        'vp9_parser_unittest.cc',
      ],
      'dependencies': [
        '../../media/base/media_base.gyp:media_base',
        '../../testing/gmock.gyp:gmock',
        '../../testing/gtest.gyp:gtest',
        '../test/media_test.gyp:media_test_support',
        'codecs',
      ],
    },
  ],
}
